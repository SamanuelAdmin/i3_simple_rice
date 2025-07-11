#!/bin/sh

info=$(acpi -b)
echo "${info#*\,}" | sed 's/,/ -/g'
