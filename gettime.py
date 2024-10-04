from datetime import datetime, timedelta, timezone
import time
import re

# !time provides a number of tools for getting the time in various timezones and converting times between timezones
# !time or !time ET will get the current EVE server time
# !time [timezone] (eg. "!time PST" or "!time CET") will get the current time in the given timezone
# !time [country abbr.] (eg. "!time US" or "!time GB") will get the current time for the given country
# In the event the given country crosses multiple timezones (eg. US), the timezone closest to mean for the country will be given
# Multiple timezones can be passed to give times across timezones
# !time [time] [destination timezone(s)] converts the given server time to the destination timezone(s)
# !time [source timezone] [time] [destination timezone(s)] converts the given time from the source timezone to the destination timezone(s)

# Dictionary of timezones, includes both timezone names and country names
timezones = {
    "ACST":9.5, "ACDT":10.5, "AEST":10, "AEDT":11, "AKST":-9, "AKDT":-8, "AST":-4, "ADT":-3, "AWST":8, "CAT":2, "CET":1, "CEST":2, "CHST":10, "CST":-6, "CDT":-5, "EAT":3, "EET":2, "EEST":3, "EST":-5, "EDT":-4, "GMT":0, "IST":1, "BST":1, "HKT":8, "HST":-10, "HDT":-9, "IST":2, "IDT":3, "JST":9, "KST":9, "MSK":3, "MST":-7, "MDT":-6, "NST":-3.5, "NDT":-2.5, "NZST":12, "NZDT":13, "PKT":5, "PST":-8, "PDT":-9, "SAST":2, "SST":-11, "UTC":0, "WAT":1, "WET":0, "WEST":1, "WIB":7, "WIT":9, "WITA":8, "ET":-1, "AD":1, "AE":4, "AF":4.5, "AG":-4, "AI":-4, "AL":1, "AM":4, "AO":1, "AQ":-3, "AR":-3, "AS":-11, "AT":1, "AU":10, "AW":-4, "AX":2, "AZ":4, "BA":1, "BB":-4, "BD":6, "BE":1, "BF":0, "BG":2, "BH":3, "BI":2, "BJ":1, "BL":-4, "BM":-4, "BN":8, "BO":-4, "BQ":-4, "BR":-3, "BS":-5, "BT":6, "BW":2, "BY":3, "BZ":-6, "CA":-5, "CC":6.5, "CD":1, "CF":1, "CG":1, "CH":1, "DE":1, "CI":0, "BF":0, "CK":-10, "CL":-4, "CM":1, "CN":8, "CO":-5, "CR":-6, "CU":-5, "CV":-1, "CW":-4, "CX":7, "CY":2, "CZ":1, "DJ":3, "DK":1, "DM":-4, "DO":-4, "DZ":1, "EC":-5, "EE":2, "EG":2, "EH":1, "ER":3, "ES":1, "ET":-1, "FI":2, "FJ":12, "FK":-3, "FM":10, "FO":0, "FR":1, "GA":1, "GB":0, "GG":0, "GD":-4, "GE":4, "GF":-3, "GG":0, "GH":0, "GI":1, "GL":-2, "GM":0, "GN":0, "GP":-4, "GQ":1, "GR":2, "GS":-2, "GT":-6, "GU":10, "GW":0, "GY":-4, "HK":8, "HN":-6, "HR":1, "HT":-5, "HU":1, "ID":7, "IE":0, "IL":2, "IM":0, "IN":5.5, "IO":6, "IQ":3, "IR":3.5, "IS":0, "IT":1, "JE":0, "JM":-5, "JO":3, "JP":9, "KE":3, "KM":3, "KN":-4, "KP":9, "KR":9, "KW":3, "KY":-5, "KZ":5, "LA":7, "LB":2, "LC":-4, "LI":1, "LK":5.5, "LR":0, "LS":2, "LT":2, "LU":1, "LV":2, "LY":2, "MA":1, "MC":1, "MD":2, "ME":1, "MF":-4, "MG":3, "MH":12, "MK":1, "ML":0, "MM":6.5, "MN":7, "MO":8, "MP":10, "MQ":-4, "MR":0, "MS":-4, "MT":1, "MU":4, "MV":5, "MW":2, "MX":-6, "MY":8, "MZ":2, "NA":2, "NC":11, "NE":1, "NF":11, "NG":1, "NI":-6, "NL":1, "NO":1, "NP":5.75, "NR":12, "NU":-11, "NZ":12, "OM":4, "PA":-5, "PE":-5, "PF":-9.5, "PG":10, "PH":8, "PK":5, "PL":1, "PM":-3, "PN":-8, "PR":-4, "PS":2, "PT":0, "PW":9, "PY":-4, "QA":3, "RE":4, "RO":2, "RS":1, "RU":3, "SA":3, "SB":11, "SC":4, "SD":2, "SE":1, "SG":8, "SH":0, "SI":1, "SJ":1, "SK":1, "SL":0, "SM":1, "SN":0, "SO":3, "SR":-3, "SS":2, "ST":0, "SV":-6, "SX":-4, "SY":3, "SZ":2, "TC":-5, "TD":1, "TF":5, "TG":0, "TH":7, "TJ":5, "TK":13, "TL":9, "TM":5, "TN":1, "TO":13, "TR":3, "TT":-4, "TV":12, "TW":8, "TZ":3, "UA":2, "UG":3, "UM":-10, "US":-5, "UY":-3, "UZ":5, "VA":1, "VC":-4, "VE":-4, "VG":-4, "VI":-4, "VN":7, "VU":11, "WF":12, "WS":13, "YE":3, "YT":3, "ZA":2, "ZM":2, "ZW":2
}

def convert_time(args):
    # Get the current year and convert it to YC time
    years = datetime.today().year - 1898

    # Handling the case where a single timezone is passed
    if (len(args) == 1) :
        time_offset = 0

        if args[0] in timezones:
            time_offset = timezones[args[0]]
        # If the first arg is not in the timezones list, check if it is a valid time and, if so, do something with it
        else:
            return "Invalid timezone!"

        time_current = datetime.now(timezone.utc) + timedelta(hours=time_offset + 1)

        output = time_current.strftime(f"%d %b %H:%M")
        output = output[0:6] + f" YC{years} " + output[7:]  # Insert the current YC date into the time string

        return output
    else:
        # Check the first value to make sure it's a valid timezone value
        source_time_offset = 0

        if args[0] in timezones:
            source_time_offset = timezones[args[0]]
        else:
            return "Invalid timezone!"

        # Check if the first value is a timezone value
        if args[0] in timezones:
            dest_tz_offsets = []

            # Check if the second value is a valid time value
            if re.search("\d+:+\d", args[1]):
                # If so, convert args[0] timezone time value args[1] to timezones args[2:]
                source_tz_offset = None

                if args[0] in timezones:
                    source_tz_offset = timezones[args[0]]
                else:
                    return "Invalid timezone!"
                
                source_time = datetime.strptime(args[1], "%H:%M")

                for tz in args[2:]:
                    if tz in timezones:
                        dest_tz_offsets.append(timezones[tz])
                    else:
                        return "Invalid timezone!"
                
                output = ""

                for time in dest_tz_offsets:
                    time_current = source_time + timedelta(hours = (time - source_time_offset))

                    out_string = time_current.strftime(f"%H:%M") + " "

                    output += out_string
                
                return output

            # If not, just get the current time in all listed timezones
            else:
                for tz in args[0:]:
                    if tz in timezones:
                        dest_tz_offsets.append(timezones[tz])
                    else:
                        return "Invalid timezone!"
                    
                output = ""

                for time in dest_tz_offsets:
                    time_current = datetime.now(timezone.utc) + timedelta(hours = time + 1)

                    out_string = time_current.strftime(f"%d %b %H:%M")
                    out_string = out_string[0:6] + f" YC{years} " + out_string[7:] + ", "

                    output += out_string
                
                return output
        
        # Check if the first value is a valid time value
        elif re.search("\d+:+\d", args[0]):
            source_time = datetime.strptime(args[1])
        else:
            return "Invalid time!"
