import argparse
import ConfigParser
import json
import swagger_client
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
from swagger_client.models.ip_block import IpBlock
from swagger_client.models.ip_pool import IpPool
from swagger_client.models.ip_pool_subnet import IpPoolSubnet
from swagger_client.models.ip_pool_range import IpPoolRange
from swagger_client.models.tag import Tag
from argparse import RawTextHelpFormatter
from libutils import check_for_parameters,find_transport_zone,parse_tags

def create_ip_block(client, name, cidr, tag):

    ip_block = IpBlock(display_name=name, cidr=cidr, tags=parse_tags(tag))

    api_instance = swagger_client.PoolManagementApi(client)
    return api_instance.create_ip_block(ip_block)

def _create_ip_block(client, **kwargs):
    needed_params = ['name', 'cidr']
    if not check_for_parameters(needed_params, kwargs):
        return None

    result = create_ip_block(client, kwargs['name'], kwargs['cidr'], kwargs['tag'])

    if result and kwargs['verbose']:
        print result
    elif result:
        print 'IP Block {} created with CIDR {}'.format(kwargs['name'], kwargs['cidr'])
    else:
        print 'Creation of IP Block {} failed for CIDR {}'.format(kwargs['name'], kwargs['cidr'])

def create_ip_pool(client, name, cidr, start, end, tag, external):

    ip_pool = IpPool(display_name=name, tags=parse_tags(tag), subnets=[IpPoolSubnet(cidr=cidr, allocation_ranges=[IpPoolRange(start=start, end=end)])])
    if external and external == 'true':
        ip_pool.tags.append(Tag(scope='external', tag='true'))

    api_instance = swagger_client.PoolManagementApi(client)
    return api_instance.create_ip_pool(ip_pool)

def _create_ip_pool(client, **kwargs):
    needed_params = ['name', 'cidr', 'start', 'end']
    if not check_for_parameters(needed_params, kwargs):
        return None

    result = create_ip_pool(client, kwargs['name'], kwargs['cidr'], kwargs['start'], kwargs['end'], kwargs['tag'], kwargs['external'])

    if result and kwargs['verbose']:
        print result
    elif result:
        print 'IP Pool {} created with CIDR {}'.format(kwargs['name'], kwargs['cidr'])
    else:
        print 'Creation of IP Pool {} failed for CIDR {}'.format(kwargs['name'], kwargs['cidr'])



def construct_parser(subparsers):
    parser = subparsers.add_parser('pool', description="Functions for ip pools",
                                   help="Functions for ip pools",
                                   formatter_class=RawTextHelpFormatter)

    parser.add_argument("command", help="""
    create_ip_block: create a new ip block
    create_ip_pool: create a new ip pool
    """)

    parser.add_argument("-c",
                        "--cidr",
                        help="CIDR for the ip block")
    parser.add_argument("-n",
                        "--name",
                        help="display name of the ip block")
    parser.add_argument("-s",
                        "--start",
                        help="Starting IP address for a range")
    parser.add_argument("-e",
                        "--end",
                        help="Ending IP address for a range")
    parser.add_argument("-external",
                        "--external",
                        help="Are the IPs in the pool external facing? (true|false)")
    parser.add_argument("-tag",
                        "--tag",
                        help="Tag to be added in the form 'key=value'",
                        action="append")

    parser.set_defaults(func=_switching_main)


def _switching_main(args):
    if args.debug:
        debug = True
    else:
        debug = False

    config = ConfigParser.ConfigParser()
    assert config.read(args.ini), 'could not read config file {}'.format(args.ini)

    configuration = Configuration()
    configuration.host = config.get('nsxv', 'nsx_manager')
    configuration.username = config.get('nsxv', 'nsx_username')
    configuration.password = config.get('nsxv', 'nsx_password')
    configuration.verify_ssl = False
    client = ApiClient(configuration)

    try:
        command_selector = {
            'create_ip_block': _create_ip_block,
            'create_ip_pool': _create_ip_pool,
            }
        command_selector[args.command](client, cidr=args.cidr,
                                       name=args.name, tag=args.tag,
                                       start=args.start, end=args.end,
                                       external=args.external, verbose=args.verbose)
    except KeyError:
        print('Unknown command')


def main():
    main_parser = argparse.ArgumentParser()
    subparsers = main_parser.add_subparsers()
    construct_parser(subparsers)
    args = main_parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
