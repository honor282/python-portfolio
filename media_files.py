def mediafiles(file_sizes, disk_caps):
    
    n = len(file_sizes)    # Number of files
    m = len(disk_caps)     # Number of disks

    remaining = disk_caps[:]        # Remaining space on each disk
    file_to_disk = [-1] * n         # -1 means file not placed

    # Greedy placement loop
    for idx, size in enumerate(file_sizes):
        best_disk = -1
        best_leftover = float('inf')

        # Check all disks to find the best fit
        for j in range(m):
            if remaining[j] >= size:                # Disk can fit the file
                leftover = remaining[j] - size
                if leftover < best_leftover:        # Better fit found
                    best_leftover = leftover
                    best_disk = j

        # Place file on best-fit disk if found
        if best_disk != -1:
            file_to_disk[idx] = best_disk
            remaining[best_disk] -= size
        else:
            print(f"⚠️ File {idx} (size {size} MB) cannot be stored on any disk.")

    return file_to_disk, remaining


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    file_sizes = [33, 14, 9, 7, 3, 1]
    disk_caps = [10, 15, 20]

    mapping, remaining = mediafiles(file_sizes, disk_caps)

    print("\n=== Media File → Disk Mapping ===")
    for i, disk in enumerate(mapping):
        print(f"File {i} ({file_sizes[i]} MB) → Disk {disk}")

    print("\nRemaining space per disk:")
    for j, space in enumerate(remaining):
        print(f"Disk {j}: {space} MB free")

    print("\nTotal unused space:", sum(remaining), "MB")
