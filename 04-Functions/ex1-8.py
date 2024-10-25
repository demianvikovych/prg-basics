def time_string(hours, minutes, time_format):
    
    if time_format=='24' :
        hours,minutes =str(hours), str(minutes)
        return f'{hours}:{minutes}'
    elif time_format=='24' and hours<10:
        hours,minutes =str(hours), str(minutes)
        return f'0{hours}:{minutes}'
    elif time_format=='12' and 10<=hours<12:
        hours,minutes =str(hours), str(minutes)
        return f'{hours}:{minutes}am'
    elif time_format=='12' and hours<10:
        hours,minutes =str(hours), str(minutes)
        return f'0{hours}:{minutes}am'
    elif time_format=='12' and 12<=hours<24:
        hours,minutes =str(hours-12), str(minutes)
        return f'{hours}:{minutes}pm'
print(time_string(16, 38, '12'))
    