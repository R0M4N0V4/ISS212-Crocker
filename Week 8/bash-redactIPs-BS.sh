#! C:\Program Files\Git\bin\sh.exe

# Emmylee Crocker - March 15, 2025
# ISS 212 CS Scripting - WK 8 TD 6 - Bash & Regex - IP Redaction
# Bash script using Regex -- Redacting data using pattern matching
# Citation - Uses ISS 212 Walthrough material

# Redact IP addresses in access.log and save to access_redacted.log
sed -E 's/[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/[REDACTED]/g' access.log > access_redacted.log

echo "Redacted IP addresses in access.log and saved as access_redacted.log"
