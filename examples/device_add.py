#!/usr/bin/python

import argparse
import json
from logicmonitor_core.Host import Host


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--company",
                        help="LogicMonitor account",
                        required=True)
    parser.add_argument('-t', '--accessid',
                        help="API Token Access Id",
                        required=True)
    parser.add_argument('-k', '--accesskey',
                        help="API Token Access Key",
                        required=True)
    parser.add_argument("-C", "--collector",
                        help="Collector FQDN",
                        required=True)

    parser.add_argument("-H", "--hostname",
                        help="Device hostname")
    parser.add_argument("-d", "--displayname",
                        help="Device display name")
    parser.add_argument("--description",
                        help="Text description of the host")
    parser.add_argument("-P", "--properties",
                        help="A dictionary of device properties to set",
                        type=json.loads)
    parser.add_argument("-g", "--groups",
                        help="Groups the device should be a member of",
                        nargs='+',)
    parser.add_argument("-a", "--alertenable",
                        help="Turn alerting on or off")
    args = parser.parse_args()

    params = {}
    params["alertenable"] = True
    params["collector"] = None
    params["description"] = ""
    params["displayname"] = None
    params["duration"] = 30
    params["fullpath"] = None
    params["groups"] = None
    params["hostname"] = None
    params["properties"] = {}
    params["starttime"] = None

    # Required params
    params["company"] = args.company
    params['accessid'] = args.accessid
    params['accesskey'] = args.accesskey
    params["collector"] = args.collector

    # Optional params
    if args.hostname is not None:
        params["hostname"] = args.hostname
    if args.displayname is not None:
        params["displayname"] = args.displayname
    if args.description is not None:
        params["description"] = args.description
    if args.properties is not None:
        params["properties"] = args.properties
    if args.groups is not None:
        params["groups"] = args.groups
    if args.alertenable is not None:
        params["alertenable"] = args.alertenable

    h = Host(params)

    exit_code = h.add()

    return exit_code

main()
