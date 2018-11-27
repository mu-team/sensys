Sen(try)Sys(log)
===============================

Raven Python Syslog Client (sentry messaging through syslog).

### System requirements

```bash
python --version == 3.4.*, 3.5.*, 3.6.*
```

### Installation

Parameter `SEPARATOR` - how plugin must separate `syslogtag` from `msg` body.

```bash
${PWD}/scripts/install.sh SEPARATOR

# new map will be copied with --backup=numbered option
sudo vim /etc/sensys/map.json  # configure mapping

sudo systemctl restart rsyslog.service
```

### Todo

1. Update deployment script;
2. Make plugin as binary.
