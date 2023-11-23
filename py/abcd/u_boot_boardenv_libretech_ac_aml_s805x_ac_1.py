# TODO: add eMMC to the board and add the tests

# checks max gpios on both bank
# toggles the led gpio
# gets a gpio at 1 (AO2) and a gpio a 0 (AO3)
env__gpio_dev_config = {
        'gpio_str_count':2 ,
        'gpio_str_1': 'aobus-banks9',
        'gpio_str_2': 'periphs-banks99',
        'gpio_op_pin': 'aobus-banks2',
        'gpio_ip_pin_set':'aobus-banks2',
        'gpio_ip_pin_clear':'aobus-banks3',
        'gpio_clear_value': 'value is 0',
        'gpio_set_value': 'value is 1',
}

env__net_dhcp_server = True

env__net_tftp_readable_file = {
	"fn": "grubaa64.efi",
	"size": 4288512,
	"crc32": "c79bc066",
}

env__efi_loader_helloworld_file = {
	'fn': 'helloworld.efi',
	'size': 12720,
	'crc32': 'b6fd8a74',
	'addr': 0x08080000,
}

env__efi_loader_grub_file = {
	"fn": "grubaa64.efi",
	"size": 4288512,
	"crc32": "c79bc066",
	'addr': 0x08080000,
}

# TODO: add eMMC to board
#env__amlogic_usb_dev_ports = (
#    {
#        'fixture_id': 'micro_b',
#        'tgt_usb_ctlr': '0',
#    },
#)

#env__amlogic_block_devs = (
#    {
#        'fixture_id': 'sd',
#        'type': 'mmc',
#        'id': '0'
#    },
#)
#