1..2 | ForEach-Object -Parallel {
	if ($_ -eq 1) {
		.\"mohr's_circle_diagram.py"
	} else {
		.\"mohr's_circle_diagram_2.py"
	}
} -ThrottleLimit 2