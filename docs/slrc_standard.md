# SLRC Standard

The **SLRC (Segmented Lyrics)** format is a text-based format for storing song lyrics with precise timing information. It is inspired by the traditional `.lrc` format but introduces the concept of **segments** and **word-level timing**.

This document describes the structure and rules of SLRC files.

---

## File Structure

An SLRC file is composed of **segments**, separated by a single line containing a single `-` character:

```
## [00:00.00]{Introduction}
-
[00:31.14][Allons]
[00:31.52][enfants]
[00:32.15][de]
[00:32.40][la]
[00:32.65][Patrie,]
-
[00:33.51][Le]
[00:33.75][jour]
[00:34.02][de]
[00:34.25][gloire]
[00:34.60][est]
[00:34.90][arrivé !]
...

```

### Segments

- Each **segment** corresponds to a small portion of the song, often a line or phrase.
- Segments are separated by a line containing only `-`.

### Lines within a Segment

Each segment consists of multiple **lines**, each representing either:

1. **A word or syllable of lyrics**
2. **A narration or note**

---

## Line Syntax

### Lyrics Line

```
[MM:SS.MM][word]
```

or

```
[HH:MM:SS.MM][word]
```

- `[MM:SS.MM]` or `[HH:MM:SS.MM]` indicates the **time offset** in the song.
- `word` is the lyric text for that timestamp.
- Each word should be on a separate line.

**Example:**

```
[00:31.14][Allons]
[00:32.15][enfant]
[00:33.12][de]
[00:33.36][la]
[00:33.51][patrie]
```

### Narration Line

```
[MM:SS.MM]{text}
```

or

```
[HH:MM:SS.MM]{text}
```

- Narrations or stage directions (e.g., `Introduction`, `Chorus`) are enclosed in `{}` instead of `[]`.
- Narrations can appear anywhere in the SLRC file.
- These lines are used to provide context or instructions, not sung lyrics.

**Example:**

```
[00:00.00]{Introduction}
```

---

## Timing Rules

1. **Chronological order**: All times in a segment must increase or stay the same.
2. **Duration calculation**: The duration of a word or narration is implicitly defined as the difference between its timestamp and the next timestamp in the same segment. For the last line in a segment, the duration is until the first timestamp of the next segment.
3. **Formats**:
   - `MM:SS.MM` → minutes:seconds.milliseconds
   - `HH:MM:SS.MM` → hours:minutes:seconds.milliseconds (for very long tracks)

---

## Segment Separator

- A single line containing only a `-` separates segments.
- No additional spaces or characters are allowed on the separator line.

**Example:**

```
[00:31.14][Allons]
[00:31.52][enfants]
[00:32.15][de]
[00:32.40][la]
[00:32.65][Patrie,]
-
[00:33.51][Le]
[00:33.75][jour]
[00:34.02][de]
[00:34.25][gloire]
[00:34.60][est]
[00:34.90][arrivé !]
```

---

## Notes

- **UTF-8 encoding** is recommended to support special characters in lyrics.
- **Empty lines** within a segment are ignored.
- SLRC is **case-sensitive** for words and narrations.
- Avoid special characters in lyrics that may conflict with parsers unless escaped properly.

---

## Summary

- `[time][word]` → Lyrics word with timestamp
- `[time]{text}` → Narration or stage direction
- `-` → Segment separator
- Chronological timestamps define durations
- UTF-8 encoded text file

For examples and conversion into LuaU, see the `script.py` in **HV Lyrics Generator**.
