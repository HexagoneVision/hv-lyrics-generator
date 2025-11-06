import re
import sys

# ANSI codes for INFO and ERROR
INFO_PREFIX = "\033[97;44m INFO \033[0m"  # White text on blue background
ERROR_PREFIX = "\033[97;41m ERROR \033[0m"  # White text on red background
RED_TEXT = "\033[91m"
RESET = "\033[0m"

def parse_time(time_str):
    parts = time_str.split(":")
    if len(parts) == 2:
        minutes = int(parts[0])
        seconds = float(parts[1])
        return minutes * 60 + seconds
    elif len(parts) == 3:
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = float(parts[2])
        return hours * 3600 + minutes * 60 + seconds
    else:
        raise ValueError(f"Unknown time format: {time_str}")

def escape_lua_string(s):
    return s.replace('"', '\\"')

def log_info(slrc_file, luau_file, song_name, song_author, sound_id):
    print(f"{INFO_PREFIX} Input parameters:")
    print(f"{INFO_PREFIX}  .slrc file: {slrc_file}")
    print(f"{INFO_PREFIX}  Output .luau file: {luau_file}")
    print(f"{INFO_PREFIX}  Song Name: {song_name}")
    print(f"{INFO_PREFIX}  Song Author: {song_author}")
    print(f"{INFO_PREFIX}  Roblox Asset ID: {sound_id}")

def log_error(message):
    print(f"{ERROR_PREFIX} {RED_TEXT}{message}{RESET}")

def slrc_to_luau(slrc_file, luau_file, song_name, song_author, sound_id):
    try:
        with open(slrc_file, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        log_error(f"Cannot read input file '{slrc_file}': {e}")
        return

    segments_raw = content.split("-\n")
    all_segments = []

    for segment in segments_raw:
        lines = [line.strip() for line in segment.strip().splitlines() if line.strip()]
        if not lines:
            continue

        times, texts, narratives = [], [], []

        for line in lines:
            match = re.match(r"\[(.*?)\]\[(.*?)\]", line)
            if match:
                time_str, text = match.groups()
                times.append(parse_time(time_str))
                texts.append(text)
                narratives.append(False)
            else:
                match_narr = re.match(r"\[(.*?)\]\{(.*?)\}", line)
                if match_narr:
                    time_str, text = match_narr.groups()
                    times.append(parse_time(time_str))
                    texts.append(text)
                    narratives.append(True)

        if times:
            all_segments.append({"times": times, "texts": texts, "narratives": narratives})

    lyrics = []
    for i, segment in enumerate(all_segments):
        times = segment["times"]
        texts = segment["texts"]
        narratives = segment["narratives"]
        durations = []

        for j in range(len(times)):
            if j < len(times) - 1:
                durations.append(times[j + 1] - times[j])
            else:
                if i < len(all_segments) - 1:
                    next_time = all_segments[i + 1]["times"][0]
                    durations.append(next_time - times[j])
                else:
                    durations.append(4)

        segment_entry = {
            "time": times[0],
            "segments": [
                {"text": escape_lua_string(text), "duration": dur, **({"narrative": True} if narrative else {})}
                for text, dur, narrative in zip(texts, durations, narratives)
            ]
        }
        lyrics.append(segment_entry)

    try:
        with open(luau_file, "w", encoding="utf-8") as f:
            f.write("local Song = {}\n\n")
            f.write(f"Song.Name = \"{escape_lua_string(song_name)}\"\n")
            f.write(f"Song.Author = \"{escape_lua_string(song_author)}\"\n")
            f.write(f"Song.SoundId = \"rbxassetid://{escape_lua_string(sound_id)}\"\n\n")
            f.write("Song.Lyrics = {\n")
            for segment in lyrics:
                f.write("\t{\n")
                f.write(f"\t\ttime = {segment['time']:.3f},\n")
                f.write("\t\tsegments = {\n")
                for s in segment["segments"]:
                    f.write(f"\t\t\t{{ text = \"{s['text']}\", duration = {s['duration']:.3f}")
                    if s.get("narrative"):
                        f.write(", narrative = true")
                    f.write(" },\n")
                f.write("\t\t},\n")
                f.write("\t},\n")
            f.write("}\n\nreturn Song\n")
    except Exception as e:
        log_error(f"Cannot write output file '{luau_file}': {e}")
        return

def parse_args():
    args = sys.argv[1:]
    params = {}
    i = 0
    while i < len(args):
        if args[i].startswith("--") and i + 1 < len(args):
            key = args[i][2:].lower()
            params[key] = args[i + 1]
            i += 2
        else:
            i += 1
    return params

if __name__ == "__main__":
    params = parse_args()
    
    slrc_file = params.get("input") or input("Enter path to .slrc file: ")
    luau_file = params.get("output") or input("Enter output .luau file path: ")
    song_name = params.get("name") or input("Enter song name: ")
    song_author = params.get("author") or input("Enter song author: ")
    sound_id = params.get("id") or input("Enter Roblox asset ID (numeric only): ")

    log_info(slrc_file, luau_file, song_name, song_author, sound_id)
    slrc_to_luau(slrc_file, luau_file, song_name, song_author, sound_id)
