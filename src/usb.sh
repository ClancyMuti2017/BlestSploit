REMOVABLE_DRIVES=""
for _device in /sys/block/*/device; do
    if echo $(readlink -f "$_device")|egrep -q "usb"; then
        _disk=$(echo "$_device" | cut -f4 -d/)
        REMOVABLE_DRIVES="$REMOVABLE_DRIVES $_disk"
    fi
done
echo "$REMOVABLE_DRIVES"
# is_usb_device() {
#     local device_path=$1 
#     for devlink in /dev/disk/by-id/usb*; do
#         if [ "$(readlink -f "$devlink")" = "$device_path" ]; then
#             return 0
#         fi
#     done
#     return 1
# }
# if is_usb_device "/dev/sdg"; then
#     echo "'/dev/sdg' bir USB cihazıdır"
# else
#     echo "'/dev/sdg' bir USB cihazı değil"
# fi