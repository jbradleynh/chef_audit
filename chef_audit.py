#!/usr/bin/env python

import optparse
import chef
import sys

def run_audit(search_string,output_file):
    
    FH = open(output_file,"w")
    FH.write("%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s\n" % (
        "name",
        "dc_city",
        "dc_name",
        "dc_region",
        "dc_cluster",
        "cpu_model_name",
        "cpu_count",
        "cpu_cores",
        "cpu_totalcores",
        "memory_total",
        "bios_revision",
        "bios_release_date",
        "bios_version",
        "system_manufacturer",
        "system_product_name",
        "system_serial_number",
        "ip6address",
        "ipaddress",
        "kernel_name",
        "kernel_release",
        "lsb_codename",
        "os",
        "os_version",
        "os_updates_security",
        "os_updates_total",
        "platform",
        "platform_family",
        "platform_version",
        "virtualization_role",
        "virtualization_system"
        )
    )
    api_obj = chef.autoconfigure()
    
    search_obj = chef.Search('node',search_string,rows=10000)

    for row in search_obj:
        # print "- %s -" % row.object.name
        FH.write("%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s\n" % (
            row.object.name,
            row.get("normal",{}).get("datacenter",{}).get("city","n/a"),
            row.get("normal",{}).get("datacenter",{}).get("name","n/a"),
            row.get("normal",{}).get("datacenter",{}).get("region","n/a"),
            row.get("normal",{}).get("datacenter",{}).get("cluster","n/a"),
            row.get("automatic",{}).get("cpu",{}).get("0",{}).get("model_name","n/a"),
            row.get("automatic",{}).get("cpu",{}).get("real","n/a"),
            row.get("automatic",{}).get("cpu",{}).get("cores","n/a"),
            row.get("automatic",{}).get("cpu",{}).get("total","n/a"),
            row.get("automatic",{}).get("memory",{}).get("total","n/a"),
            row.get("automatic",{}).get("dmi",{}).get("bios",{}).get("bios_revision","n/a"),
            row.get("automatic",{}).get("dmi",{}).get("bios",{}).get("release_date","n/a"),
            row.get("automatic",{}).get("dmi",{}).get("bios",{}).get("version","n/a"),
            row.get("automatic",{}).get("dmi",{}).get("system",{}).get("manufacturer","n/a"),
            row.get("automatic",{}).get("dmi",{}).get("system",{}).get("product_name","n/a"),
            row.get("automatic",{}).get("dmi",{}).get("system",{}).get("serial_number","n/a"),
            row.get("automatic",{}).get("ip6address","n/a"),
            row.get("automatic",{}).get("ipaddress","n/a"),
            row.get("automatic",{}).get("kernel",{}).get("name","n/a"),
            row.get("automatic",{}).get("kernel",{}).get("release","n/a"),
            row.get("automatic",{}).get("lsb",{}).get("codename","n/a"),
            row.get("automatic",{}).get("os","n/a"),
            row.get("automatic",{}).get("os_version","n/a"),
            row.get("automatic",{}).get("os_updates",{}).get("security","n/a"),
            row.get("automatic",{}).get("os_updates",{}).get("total","n/a"),
            row.get("automatic",{}).get("platform","n/a"),
            row.get("automatic",{}).get("platform_family","n/a"),
            row.get("automatic",{}).get("platform_version","n/a"),
            row.get("automatic",{}).get("virtualization",{}).get("role","n/a"),
            row.get("automatic",{}).get("virtualization",{}).get("system","n/a"),
            )
        )
    # be sure to close
    FH.close

if __name__=="__main__":
    parser = optparse.OptionParser()
    parser.add_option("-s", "--search", dest="search", type="string", default=None, help="knife node search string")
    parser.add_option("-o", "--output", dest="output", type="string", default=None, help="output file name")
    (opt, args) = parser.parse_args()

    if opt.search == None or opt.output == None:
        parser.print_help()
        sys.exit(2)
    else:
        run_audit(opt.search, opt.output)
