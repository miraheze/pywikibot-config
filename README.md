# Pywikibot config

Pywikibot config for [User:BeeBot](https://meta.miraheze.org/wiki/User:BeeBot). Contains crontab config and family configuration.

Infrastructure Specialists have push access. This repo is pulled by puppet automatically.

# Adding new crontab entries

In cron.yaml, crontab entries for your wiki is added as arrays in a top level key, where that top level key must be your wiki's database name, and each individual array results in a crontab entry.

Example:

```yaml
metawiki: # your wiki's database name
  - name: 'archivebot-job' # MUST BE UNIQUE, no other crontab entry for your wiki must have the same name
    ensure: 'present' # present to enable, absent to disable
    script: 'archivebot' # Pywikibot script you want to run
    scriptparams: 'Template:Autoarchive/config' # parameters for that script, set to '' if there are no parameters
    hour: '0' # regular crontab parameters
    minute: '0'
    month: 'absent' # absent = *
    monthday: 'absent'
    weekday: 'absent'
```

Results in `0 0 * * * pwb.py archivebot Template:Autoarchive/config -lang:metawiki`

All parameters from the example must be present!

# Adding langs

All wikis are part of the `wikitide` family in the Pywikibot config. Langs are used to select wikis based on their database name, as it is a unique identifier for wikis on Miraheze.

They only have one parameter: `domain`, which is the domain for the wiki.

Example:

```yaml
metawiki:
  domain: 'meta.miraheze.org'
```

# License

Licensed under the GPL 3.0 or later.
