Setup

  $ export SHEET_FILE=$CRAMTMP/sheet-stop
  $ alias ti="ti --no-color"

Running stop when not working

  $ ti stop
  For all I know, you aren't working on anything. I don't know what to do.
  See `ti -h` to know how to start working.
  [1]

Incorrectly running it (above) shouldn't create any file

  $ test -f $SHEET_FILE
  [1]

Start a task and then stop

  $ ti on testing-my-foot
  Start working on testing-my-foot.
  $ ti stop
  So you stopped working on testing-my-foot.
  $ test -f $SHEET_FILE

stop a tagged activity

  $ ti on tagged-one
  Start working on tagged-one.
  $ ti tag woohoo
  Okay, tagged current work with 1 tag.
  $ ti stop
  So you stopped working on tagged-one.

Check the current file existence

  $ ti on awesomeness
  Start working on awesomeness.
  $ ti stop
  So you stopped working on awesomeness.
  $ test -f $SHEET_FILE
