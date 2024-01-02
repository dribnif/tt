# Change overview
# 1.1.1
  **ect | edit-current-timebox** fix: UTC datetime was being displayed in the comment when editing the current timebox
# 1.1.0
  **ect | edit-current-timebox** new command that allows you to edit the notes within your timebox from an
  editor of your choice
# 1.0.11
  **log** improvement: allow the user to define a timebox for which to display logged activities
  **report** improvements: report all activities if none specified, also consider the value of TT_HOURS_PER_DAY
  when coloring in the total amount of hours worked
  **help** updates to reflect the new functionality that was added
  other minor bugfixes
  Most of the features contributed by [chigozienri](https://github.com/chigozienri)

# 1.0.6
* **calview** improvement: show in progress timebox as well, assuming end-time to be "now"

# 1.0.4
* **calview** improvement: show weekend (Saturday and Sunday) in matrix view, if time has been logged on weekends. 
  Otherwise default to 5 day, Monday to Friday week. Contributed by [nedimAT](https://github.com/nedimAT).

# 1.0.3
* as of this version, the end time of an entry must be **after** the start time of said entry
