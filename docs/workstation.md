# Optional workstation choices

These project decisions remain part of Phosphor Studio. They are separate from
the installable theme and are not applied automatically.

| Area | Intended configuration |
| --- | --- |
| Agents | Codex and Claude with equal prominence |
| Bar | One native Agents widget; no duplicate workspace widget |
| Agent menu | Two named launch entries, Codex and Claude |
| Clock | Centered AM/PM clock; proposed format `ddd h:mm AP` |
| Updates | Native Omarchy update indicator enabled |
| Existing widgets | Preserve current sections, relative order and settings |
| Usage reporting | Codex/Claude enabled, native 900-second refresh, sync off |
| Default agent and accounts | Preserve the user's selection and credentials |
| Idle, monitors and shortcuts | Preserve existing configuration |

The native Agents widget reports usage/limits; that is not live task state.
It may hide when no usage records are available. Installed provider support
must be checked against the user's Omarchy version.

The native terminal launch paths used in the earlier design were:

```bash
omarchy launch terminal codex
omarchy launch terminal claude
```

They start the selected CLI and retain its permission behavior. Review the
working directory before starting project work; no automatic approval flags,
agent installation or sign-in are part of the theme.

## Status and preservation

The optional profile has not been applied to the daily desktop. Bar density,
native-control placement, windows, notifications and agent shortcuts remain
under review. Login, lock-screen redesign and screensaver work are separate.

The earlier helper, configuration fragments and tests are preserved in Git
history at [e7c6181](https://github.com/mapski/omarchy-haldo-phosphor-theme/tree/e7c618184d363e73e6c4c11e1d0acf225ae3c4a1/profiles)
and in the project author's local development archive. They are historical
material, not files provided by the current installation. The earlier bar
profile can duplicate custom workspaces or omit native controls; do not apply
it without reconciling it with the actual desktop configuration.

Future companion setup must be documented and reviewed separately. No Python
helper, test script or profile installer is shipped in this theme.
