# firmware_update
check the result of firmware update
问题背景：
  1、网卡固件升级过程中，如果检查到当前网卡固件的eeprom id与nvmupdate.cfg中已有的eeprom id不一致（或不在nvmupdate.cfg配置文件中），则会停止固件升级。
  2、网卡来料无法控制，无法确定网卡固件的eeprom rom。
解决办法：，
  1、将报错提供的eeprom id写入nvmupdate.cfg配置文件中，eeprom id 校验一致使网卡固件升级成功。
