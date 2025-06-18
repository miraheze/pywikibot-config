# Pywikibot config

Pywikibot config for [User:BeeBot](https://meta.miraheze.org/wiki/User:BeeBot). Contains periodic jobs (systemd timers) and family configuration.

Infrastructure Specialists have push access. This repo is pulled by Puppet automatically.

---

## Adding new periodic jobs

In `periodic_jobs.yaml`, entries for your wiki are added as arrays under a top-level key. That key must be your wiki's **database name**, and each array item defines one `systemd` timer + service.

For example:

```yaml
# This example defines a job that runs every day at midnight:
metawiki:  # your wiki's database name
  - name: 'archivebot-job'  # MUST BE UNIQUE within this wiki
    ensure: 'present'  # 'present' to enable, 'absent' to disable
    script: 'archivebot'  # Pywikibot script to run
    scriptparams: 'Template:Autoarchive/config'  # Parameters to pass to the script ('' if none)
    hour: '0'  # Time fields
    minute: '0'
    month: '*'
    monthday: '*'
    weekday: '*'
```

> This job will be translated into a `systemd` timer with an `OnCalendar=*‐*‐* 00:00:00`, which means:
> _“Run the specified script every day at midnight.”_

Behind the scenes, this results in:
- a `.service` unit to run:
  ```
  /usr/local/bin/pywikibot archivebot Template:Autoarchive/config -lang:metawiki
  ```
- and a `.timer` unit that triggers it on the defined schedule.

All parameters shown in the example are **mandatory**.

---

## Adding langs

All wikis belong to the `wikitide` family in the Pywikibot configuration. Each wiki must be listed by its database name with its associated domain.

Example:

```yaml
metawiki:
  domain: 'meta.miraheze.org'
```

This mapping allows Pywikibot to target the correct wiki based on the `-lang` parameter (which corresponds to the database name).

---

## License

Licensed under the GNU General Public License v3.0 or later.  
See: https://www.gnu.org/licenses/gpl-3.0.html
