BOT_NAME = 'talengineering'

SPIDER_MODULES = ['talengineering.spiders']
NEWSPIDER_MODULE = 'talengineering.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'talengineering.pipelines.TalengineeringPipeline': 100,

}