print('fly to vulcan')




   or: git stash drop [-q|--quiet] [<stash>]
   or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]
   or: git stash branch <branchname> [<stash>]
   or: git stash clear
   or: git stash [push [-p|--patch] [-k|--[no-]keep-index] [-q|--quiet]
          [-u|--include-untracked] [-a|--all] [-m|--message <message>]
          [--pathspec-from-file=<file> [--pathspec-file-nul]]
          [--] [<pathspec>...]]
   or: git stash save [-p|--patch] [-k|--[no-]keep-index] [-q|--quiet]
          [-u|--include-untracked] [-a|--all] [<message>]

   or: git stash drop [-q|--quiet] [<stash>]
   or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]
   or: git stash branch <branchname> [<stash>]
   or: git stash clear
   or: git stash [push [-p|--patch] [-k|--[no-]keep-index] [-q|--quiet]
          [-u|--include-untracked] [-a|--all] [-m|--message <message>]
          [--pathspec-from-file=<file> [--pathspec-file-nul]]
          [--] [<pathspec>...]]
   or: git stash save [-p|--patch] [-k|--[no-]keep-index] [-q|--quiet]
          [-u|--include-untracked] [-a|--all] [<message>]

   or: git stash drop [-q|--quiet] [<stash>]
   or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]
   or: git stash branch <branchname> [<stash>]
   or: git stash clear
   or: git stash [push [-p|--patch] [-k|--[no-]keep-index] [-q|--quiet]
          [-u|--include-untracked] [-a|--all] [-m|--message <message>]
          [--pathspec-from-file=<file> [--pathspec-file-nul]]
          [--] [<pathspec>...]]
   or: git stash save [-p|--patch] [-k|--[no-]keep-index] [-q|--quiet]
          [-u|--include-untracked] [-a|--all] [<message>]

   or: git stash drop [-q|--quiet] [<stash>]
   or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]
   or: git stash branch <branchname> [<stash>]
   or: git stash clear
   or: git stash [push [-p|--patch] [-k|--[no-]keep-index] [-q|--quiet]
          [-u|--include-untracked] [-a|--all] [-m|--message <message>]
          [--pathspec-from-file=<file> [--pathspec-file-nul]]
          [--] [<pathspec>...]]
   or: git stash save [-p|--patch] [-k|--[no-]keep-index] [-q|--quiet]
          [-u|--include-untracked] [-a|--all] [<message>]




   or: git stash drop [-q|--quiet] [<stash>]
   or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]
   or: git stash branch <branchname> [<stash>]
   or: git stash clear
   or: git stash [push [-p|--patch] [-k|--[no-]keep-index] [-q|--quiet]
          [-u|--include-untracked] [-a|--all] [-m|--message <message>]
          [--pathspec-from-file=<file> [--pathspec-file-nul]]
          [--] [<pathspec>...]]
   or: git stash save [-p|--patch] [-k|--[no-]keep-index] [-q|--quiet]
          [-u|--include-untracked] [-a|--all] [<message>]


Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git stash list
stash@{0}: WIP on dev: cf464a1 add merges

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git stash apply
On branch dev
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.txt

no changes added to commit (use "git add" and/or "git commit -a")

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git stash drop
Dropped refs/stash@{0} (52040667698ef8a3054f3399d877265ccb6bc39e)

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git checkout
M       readme.txt

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ vi readme.tat

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git readme.txt
git: 'readme.txt' is not a git command. See 'git --help'.

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ vi readme.txt

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git stash apply
No stash entries found.

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git stash list

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git branch
* dev
  issue-101
  master

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git cherry -pick 6df6532
error: unknown switch `p'
usage: git cherry [-v] [<upstream> [<head> [<limit>]]]

    --abbrev[=<n>]        use <n> digits to display SHA-1s
    -v, --verbose         be verbose


Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git branch
* dev
  issue-101
  master

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git switch -c feature -vulcan
error: unknown switch `v'
usage: git switch [<options>] [<branch>]

    -c, --create <branch>
                          create and switch to a new branch
    -C, --force-create <branch>
                          create/reset and switch to a branch
    --guess               second guess 'git switch <no-such-branch>'
    --discard-changes     throw away local modifications
    -q, --quiet           suppress progress reporting
    --recurse-submodules[=<checkout>]
                          control recursive updating of submodules
    --progress            force progress reporting
    -m, --merge           perform a 3-way merge with the new branch
    --conflict <style>    conflict style (merge or diff3)
    -d, --detach          detach HEAD at named commit
    -t, --track           set upstream info for new branch
    -f, --force           force checkout (throw away local modifications)
    --orphan <new-branch>
                          new unparented branch
    --overwrite-ignore    update ignored files (default)
    --ignore-other-worktrees
                          do not check if another worktree is holding the given ref


Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git switch master
error: Your local changes to the following files would be overwritten by checkout:
        readme.txt
Please commit your changes or stash them before you switch branches.
Aborting

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git checkout master
error: Your local changes to the following files would be overwritten by checkout:
        readme.txt
Please commit your changes or stash them before you switch branches.
Aborting
   or: git stash drop [-q|--quiet] [<stash>]
   or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]
   or: git stash branch <branchname> [<stash>]
   or: git stash clear
   or: git stash [push [-p|--patch] [-k|--[no-]keep-index] [-q|--quiet]
          [-u|--include-untracked] [-a|--all] [-m|--message <message>]
          [--pathspec-from-file=<file> [--pathspec-file-nul]]
          [--] [<pathspec>...]]
   or: git stash save [-p|--patch] [-k|--[no-]keep-index] [-q|--quiet]
          [-u|--include-untracked] [-a|--all] [<message>]


Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git stash list
stash@{0}: WIP on dev: cf464a1 add merges

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git stash apply
On branch dev
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.txt

no changes added to commit (use "git add" and/or "git commit -a")

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git stash drop
Dropped refs/stash@{0} (52040667698ef8a3054f3399d877265ccb6bc39e)

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git checkout
M       readme.txt

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ vi readme.tat

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git readme.txt
git: 'readme.txt' is not a git command. See 'git --help'.

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ vi readme.txt

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git stash apply
No stash entries found.

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git stash list

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git branch
* dev
  issue-101
  master

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git cherry -pick 6df6532
error: unknown switch `p'
usage: git cherry [-v] [<upstream> [<head> [<limit>]]]

    --abbrev[=<n>]        use <n> digits to display SHA-1s
    -v, --verbose         be verbose


Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git branch
* dev
  issue-101
  master

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git switch -c feature -vulcan
error: unknown switch `v'
usage: git switch [<options>] [<branch>]

    -c, --create <branch>
                          create and switch to a new branch
    -C, --force-create <branch>
                          create/reset and switch to a branch
    --guess               second guess 'git switch <no-such-branch>'
    --discard-changes     throw away local modifications
    -q, --quiet           suppress progress reporting
    --recurse-submodules[=<checkout>]
                          control recursive updating of submodules
    --progress            force progress reporting
    -m, --merge           perform a 3-way merge with the new branch
    --conflict <style>    conflict style (merge or diff3)
    -d, --detach          detach HEAD at named commit
    -t, --track           set upstream info for new branch
    -f, --force           force checkout (throw away local modifications)
    --orphan <new-branch>
                          new unparented branch
    --overwrite-ignore    update ignored files (default)
    --ignore-other-worktrees
                          do not check if another worktree is holding the given ref


Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git switch master
error: Your local changes to the following files would be overwritten by checkout:
        readme.txt
Please commit your changes or stash them before you switch branches.
Aborting

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git checkout master
error: Your local changes to the following files would be overwritten by checkout:
        readme.txt
Please commit your changes or stash them before you switch branches.
Aborting
   or: git stash drop [-q|--quiet] [<stash>]
   or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]
   or: git stash branch <branchname> [<stash>]
   or: git stash clear
   or: git stash [push [-p|--patch] [-k|--[no-]keep-index] [-q|--quiet]
          [-u|--include-untracked] [-a|--all] [-m|--message <message>]
          [--pathspec-from-file=<file> [--pathspec-file-nul]]
          [--] [<pathspec>...]]
   or: git stash save [-p|--patch] [-k|--[no-]keep-index] [-q|--quiet]
          [-u|--include-untracked] [-a|--all] [<message>]


Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git stash list
stash@{0}: WIP on dev: cf464a1 add merges

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git stash apply
On branch dev
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.txt

no changes added to commit (use "git add" and/or "git commit -a")

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git stash drop
Dropped refs/stash@{0} (52040667698ef8a3054f3399d877265ccb6bc39e)

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git checkout
M       readme.txt

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ vi readme.tat

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git readme.txt
git: 'readme.txt' is not a git command. See 'git --help'.

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ vi readme.txt

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git stash apply
No stash entries found.

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git stash list

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git branch
* dev
  issue-101
  master

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git cherry -pick 6df6532
error: unknown switch `p'
usage: git cherry [-v] [<upstream> [<head> [<limit>]]]

    --abbrev[=<n>]        use <n> digits to display SHA-1s
    -v, --verbose         be verbose


Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git branch
* dev
  issue-101
  master

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git switch -c feature -vulcan
error: unknown switch `v'
usage: git switch [<options>] [<branch>]

    -c, --create <branch>
                          create and switch to a new branch
    -C, --force-create <branch>
                          create/reset and switch to a branch
    --guess               second guess 'git switch <no-such-branch>'
    --discard-changes     throw away local modifications
    -q, --quiet           suppress progress reporting
    --recurse-submodules[=<checkout>]
                          control recursive updating of submodules
    --progress            force progress reporting
    -m, --merge           perform a 3-way merge with the new branch
    --conflict <style>    conflict style (merge or diff3)
    -d, --detach          detach HEAD at named commit
    -t, --track           set upstream info for new branch
    -f, --force           force checkout (throw away local modifications)
    --orphan <new-branch>
                          new unparented branch
    --overwrite-ignore    update ignored files (default)
    --ignore-other-worktrees
                          do not check if another worktree is holding the given ref


Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git switch master
error: Your local changes to the following files would be overwritten by checkout:
        readme.txt
Please commit your changes or stash them before you switch branches.
Aborting

Lily_@gardenias-2018 MINGW64 ~/learngit (dev)
$ git checkout master
error: Your local changes to the following files would be overwritten by checkout:
        readme.txt
Please commit your changes or stash them before you switch branches.
Aborting
