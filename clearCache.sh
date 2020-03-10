rm -rf __pycache__
rm -rf livesite/__pycache__
clearAllCache()
{
	find . -type d -name "__pycache__" -exec rm -r {} +
}
