require 'sinatra'
require 'aws-sdk-core'

get "/" do
	dynamodb = Aws::DynamoDB::Client.new(
		region: 'us-east-1',
		credentials: Aws::Credentials.new('AKIAI6PU7IIGNUBSI26A', 'qBrlCJMywo029GlaXsLVI8Rf4286eWsC6aU+ue53')
)
	# dynamodb.list_tables
	@data = [{:time => 0, :value => 10}]
	erb :index 
end