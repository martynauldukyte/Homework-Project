def celsius_converter(f_temp):
    celsius = (float(f_temp) - 32) * 5.0 / 9.0
    return round(celsius, 2)

def parse_and_clean(line):
    parts = line.split('|')
    if len(parts) != 5:
        return None
    
    timestamp = parts[0].strip()
    station_id = parts[1].strip()
    temp_f = parts[2].strip()
    humidity = parts[3].strip()
    status = parts[4].strip()
    
    if temp_f in ["ERROR", "N/A"] or not temp_f:
        return None
        
    if status != "ACTIVE":
        return None
        
    return timestamp, station_id, temp_f, humidity, status

input_file = "environmental_raw.txt"
output_file = "environmental_clean.csv"

corrupted_count = 0

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.write("Timestamp,StationID,Temp(C),Humidity(%),Sensor_Status\n")
    
    for line in infile:
        if not line.strip():
            corrupted_count += 1
            continue
            
        cleaned_data = parse_and_clean(line)
        
        if cleaned_data is None:
            corrupted_count += 1
        else:
            timestamp, station_id, temp_f, humidity, status = cleaned_data
            temp_c = celsius_converter(temp_f)
            outfile.write(f"{timestamp},{station_id},{temp_c},{humidity},{status}\n")

print(f"How many corrupted lines were skipped: {corrupted_count}")