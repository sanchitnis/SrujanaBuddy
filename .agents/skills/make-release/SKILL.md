# Skill: make-release

## Purpose
Automate the process of creating a new SrujanaBuddy release, updating release notes, and generating/refreshing installation and upgrade scripts. Ensures all local memory/profile files are migrated or patched as needed for compatibility with the new release. Tracks new features and their impact on file/data structure for safe upgrades.

---

## Triggers
- "make a release"
- "create new release"
- "update release notes"
- "generate upgrade script"
- "migrate user data for new version"

---

## Workflow

1. **Release Preparation**
   - Collect all new features, bugfixes, and breaking changes since the last release.
   - For each new feature, require a note on whether it changes any file/data structure (e.g., new fields in profile, new folders, renamed files).
   - Update `CHANGELOG.md` and draft release notes.

2. **Compatibility & Migration**
   - For any file/data structure change, generate a migration script (Python or batch) that:
     - Detects old-format files in user folders (e.g., `profiles/`, `drive-with-gps/`).
     - Applies necessary changes (add fields, rename files, move data, etc.) to bring them up to date.
     - Logs all changes and backs up originals.
   - Add migration script to the release package.

3. **Release Creation**
   - Tag the new release in git.
   - Create a new GitHub Release with:
     - Updated release notes (from step 1)
     - Downloadable zip (source code)
     - Migration/upgrade script
     - Clear instructions for both new installs and upgrades

4. **Update Installation/Upgrade Instructions**
   - In `README.md` and `docs/Getting-Started-for-Nontechnical-Users.md`, add/refresh:
     - How to install for new users
     - How to upgrade for existing users (run migration script, move profiles, etc.)
     - Warnings about backing up data before upgrade

5. **Feature Impact Tracking**
   - For every new feature, require a checklist:
     - Does it change any file/folder/data structure?
     - If yes, is a migration needed? (Y/N)
     - If yes, is the migration script tested on old data?
   - Document this in a `release-feature-impact.md` file for each release.

---

## Output Artifacts
- Updated `CHANGELOG.md`
- Updated release notes (GitHub Release)
- Migration/upgrade script
- Updated install/upgrade instructions
- `release-feature-impact.md` for traceability

---

## Example Usage
- "make a release for v2.1"
- "add migration for new profile field"
- "generate upgrade script for v2.1"
- "update release notes and instructions"

---

## Notes
- All migration scripts must be idempotent and safe (never delete user data without backup).
- All new features must be reviewed for backward compatibility.
- Always test upgrade on a sample of old user data before publishing release.
