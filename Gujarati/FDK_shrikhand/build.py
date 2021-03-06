#! /usr/bin/env python

import hindkit as kit
kit.confirm_version('0.2.1')

# - - -

family = kit.Family(
    trademark = 'Shrikhand',
    script = 'Gujarati',
    # hide_script_name = True,
)

family.set_masters(
    masters = [kit.Master(family, 'Regular', 0)],
    modules = [
        'kerning',
        # 'mark_positioning',
        # 'mark_to_mark_positioning',
        # 'devanagari_matra_i_variants',
    ],
)

family.set_styles([('Regular', 0, 400)])

# - - -

builder = kit.Builder(family)

builder.fontrevision = '0.100'

builder.set_options([

    'prepare_styles',   # stage i
    'prepare_features', # stage ii
    'compile',          # stage iii

    'makeinstances', #!
    'checkoutlines', #!
    # 'autohint',      #!

    'do_style_linking',
    'use_os_2_version_4',
    'prefer_typo_metrics',
    'is_width_weight_slope_only',

])

builder.generate_designspace()
builder.generate_fmndb()

builder.build()
