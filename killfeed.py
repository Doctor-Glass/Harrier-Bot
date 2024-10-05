# !killfeed allows you to create and manage a feed of kills for a specific organization in a given Discord channel

# Usage:
# !killfeed create [player/corp/alliance ID] [threshold (optional)] [kills (y/n) (optional)] [losses (y/n) (optional)]
# [player/corp/alliance ID]: The ID value for the organization you want to track
# [threshold (optional)]: A minimuim threshold (in ISK) for the value of kills, below which kills/losses will not be tracked. Defaults to 10,001 to exclude blank pod kills/losses. Setting this below 10,001 will include all blank pod kills/losses
# [kills (y/n) (optional)]: Whether to include kills by the given entity. Defaults to Y.
# [losses (y/n) (optional)]: Whether to include losses by the given entity. Defaults to N.

# !killfeed edit [player/corp/alliance ID] [threshold (optional)] [kills (y/n) (optional)] [losses (y/n) (optional)]

# Passing just !killfeed [args] will default to creating a new killfeed (ie. "create") is optional but preferred.


# !killfeed remove [player/corp/alliance ID]

# !killfeed create, creates a new killfeed
def create(args):

    return

# !killfeed edit, edits an existing killfeed
def edit(args):

    return

# !killfeed remove, removes an existing killfeed
def remove(args):

    return