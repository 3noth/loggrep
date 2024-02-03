## NAME
loggrep - a utility for parsing log files with the ability to filter by keywords and identifiers.

## SYNOPSIS
**loggrep** <input_file> [options]...

## DESCRIPTION
**loggrep** is a command-line tool for analyzing and processing log files. It allows the user to filter entries by specified keywords and identifiers, as well as apply special patterns for processing lines.

## OPTIONS
- **-O, --output** <file>\
  Path to the output file for saving results. If not specified, output is sent to the console.

- **-K, --keywords** <keywords> <keywords>\
  List of keywords to search for in the logs. This parameter is required.

- **-Id** <pattern>\
  Pattern for identifying a unique identifier in log lines.

- **-Ld** <pattern>\
  Pattern for additional processing of log lines.

## EXAMPLES

Example of usage for filtering a log by the keywords "error" and "warning":\
$ loggrep logfile.log -K error warning\

Example of usage with output saved to a file:\
$ loggrep logfile.log -O output.log -K error\

$ loggrep logfile.log -K error warning -Id "user_id=\d+" -O output_folder\
$ loggrep logfile.log -K error -Ld "\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]" -O output.txt
