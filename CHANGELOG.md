# Changelog

## v0.1.0 (2022-04-13)

### New Features
Changed the API. Now `provide_dir` function takes two arguments. The path it shall provide and the sink where it outputs whether or not it already existed or if it was created. It no longer returns anything. The old functionality where you can handle the two scenarios in your user code is still available as `core_provide_dir`.

### Bug Fixes
Removed an accidental dependency on `remove_directory`

## v0.0.3 (2022-04-01)

Updated CHANGELOG.md

## v0.0.2 (2022-04-01)

Updated README.md

## v0.0.1 (2022-03-31)

Initial version.
