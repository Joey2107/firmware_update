#-_-encoding:utf-8-_-
#/usr/bin/python3.6
import subprocess
import os
import sys

log_name="event_check.log"
newlog_name = "new_event_check.log"
target_str = "Selected"
sub_str = " This is for debugging!"
firmware_tool = "./eeupdate64e"
def shell_commands(command=None):
        try:
                echo_stream = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                #print("echo_info:%s" %echo_info)
                str_info = echo_stream.stdout.read()
                event_time_stream = subprocess.Popen("date", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                event_time = event_time_stream.stdout.read()
        #       print("test time:%s" %event_time)
        #       print("test time:%s" %type(event_time))
                #无正常输出，则收集错误打印信息 
                if str_info == "":
                        err_info = echo_info.stderr.read()
                        print("error_info:", err_info)
                        return event_time, err_info#由于返回数据以元组形式返回，需转成字符类型写入

                else:
                        return event_time, str_info
        except Exception as e:
                sys.exit(e)
                #return err_time, err_stream

def service_status(command):
#       send_commands("systemct status dhcpd")
#       send_commands("systemctl status vsftpd")
#       send_commands("systemctl status tftp")
#       send_commands("./eeupdate64e")
        log = open(log_name,"wb")
#       test_date = (1, 2, 3)
#       log.write(test_date)
        #log.write(send_commands("./eeupdate64e"))
        result = shell_commands(command)
        for i in result:
                log.write(i)
        log.close()
		
def check_log():
	service_status(firmware_tool)
	log = open(log_name, "r")
	new_log = open(newlog_name, "w")
	for i in log：
		if target_str in i:
			new_i = i.replace(target_str, target_str+sub_str)
			new_log.write(new_i)
		else:
			new_log.write(i)
	new_log.close()
	log.close()
	os.replace(newlog_name, log_name)

check_log()


