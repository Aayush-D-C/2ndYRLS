# Git Cheat Sheet

This cheat sheet covers essential Git commands for quick reference.

---

## 1. **Setup and Configuration**
- `git config --global user.name "Your Name"`: Sets the global username.
- `git config --global user.email "your.email@example.com"`: Sets the global email.
- `git config --list`: Displays all Git configuration.

---

## 2. **Basic Commands**
- `git init`: Initializes a new Git repository.
- `git clone <url>`: Clones a remote repository to your local machine.
- `git status`: Shows the current status of the repository.
- `git add <file>`: Stages a file for the next commit.
- `git add .`: Stages all files in the current directory.

---

## 3. **Commit Changes**
- `git commit -m "Commit message"`: Commits staged changes with a message.
- `git commit -am "Commit message"`: Stages and commits changes in tracked files.

---

## 4. **Branching**
- `git branch`: Lists all branches.
- `git branch <branch-name>`: Creates a new branch.
- `git checkout <branch-name>`: Switches to the specified branch.
- `git checkout -b <branch-name>`: Creates and switches to a new branch.

---

## 5. **Pushing and Pulling**
- `git remote add origin <url>`: Links your local repository to a remote repository.
- `git push -u origin <branch-name>`: Pushes changes to the remote repository (first time).
- `git push`: Pushes changes to the remote repository.
- `git pull`: Pulls updates from the remote repository.

---

## 6. **Undoing Changes**
- `git reset <file>`: Unstages a staged file.
- `git reset --soft HEAD~1`: Undoes the last commit but keeps the changes staged.
- `git reset --hard HEAD~1`: Undoes the last commit and discards changes.
- `git checkout -- <file>`: Reverts a file to the last committed state.

---

## 7. **Logs and History**
- `git log`: Displays commit history.
- `git log --oneline`: Shows a condensed commit history.
- `git log --graph --all`: Displays a graphical representation of commits.

---

## 8. **Stashing**
- `git stash`: Temporarily saves changes you don’t want to commit yet.
- `git stash pop`: Applies the stashed changes.
- `git stash list`: Lists all stashes.

---

## 9. **Merging and Conflicts**
- `git merge <branch-name>`: Merges the specified branch into the current branch.
- `git mergetool`: Opens a merge conflict resolution tool.

---

## 10. **Tagging**
- `git tag <tag-name>`: Tags a specific commit.
- `git tag`: Lists all tags.
- `git push origin <tag-name>`: Pushes a tag to the remote repository.

---

## 11. **Deleting**
- `git branch -d <branch-name>`: Deletes a branch locally.
- `git push origin --delete <branch-name>`: Deletes a branch from the remote repository.

---

## Learn More
For an in-depth guide, visit: [Git Documentation](https://git-scm.com/doc)

---

##If u are using node.js or any other frameworks
- In case you are using along with dependencies then u might want some of the modules to not get uploaded in github then in that case u can add i your .gitignore use this repo to add all your .gitignore according to your need 
-https://github.com/github/gitignore

 ---