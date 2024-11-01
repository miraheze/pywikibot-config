# Pywikibot config

Pywikibot config for [User:BeeBot](https://meta.miraheze.org/wiki/User:BeeBot). Contains crontab config and family configuration.

This repo is pulled by puppet automatically.

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
