#!/bin/bash


iconhigh="audio-volume-high-symbolic"
iconmedium="audio-volume-medium-symbolic"
iconlow="audio-volume-low-symbolic"
iconmute="audio-volume-muted-symbolic"


function shnotif() 
{
	muteStatus="$(pactl get-sink-mute @DEFAULT_SINK@ | grep -oP 'yes|no')"
	currentOutValue="$(pactl get-sink-volume @DEFAULT_SINK@ | awk '/Volume:/ {print $5}' | sed 's/%//')"

	if [ "$muteStatus" = "no" ]; then
		dunstify -i $iconhigh -r 9991 --hints=int:value:$currentOutValue "Volume" "Current value: $currentOutValue%"
	else 
		dunstify -i $iconmute -r 9991 "Volume" "Volume muted"
	fi
}


function volup()
{
	pactl set-sink-volume @DEFAULT_SINK@ +2%
	shnotif
}


function voldown()
{
	pactl set-sink-volume @DEFAULT_SINK@ -2%
	shnotif
}

function volmute()
{
	pactl set-sink-mute @DEFAULT_SINK@ toggle
	shnotif
}



case $1 in
	up)
		volup
		;;
	down)
		voldown
		;;
	mute)
		volmute
		;;
esac
