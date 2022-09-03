is_usb_device() {
    local device_path=$1 
    for devlink in /dev/disk/by-id/usb*; do
        if [ "$(readlink -f "$devlink")" = "$device_path" ]; then
            return 0
        fi
    done
    return 1
}
if is_usb_device "/dev/sdg"; then
    echo "'/dev/sdg' bir USB cihazıdır"
else
    echo "'/dev/sdg' bir USB cihazı değil"
fi