require 'sinatra'
require 'aws-sdk-core'
require 'json'

get "/index?.:format?" do
	dynamodb = Aws::DynamoDB::Client.new(
		region: 'us-east-1',
		credentials: Aws::Credentials.new('AKIAI6PU7IIGNUBSI26A', 'qBrlCJMywo029GlaXsLVI8Rf4286eWsC6aU+ue53')
)
	@data = dynamodb.query({
		:table_name => '2012', 
		:consistent_read => true,
		:select => 'ALL_ATTRIBUTES',
		:key_conditions => { 
		  'Ticker' => { 
		    :comparison_operator => 'EQ', 
		    :attribute_value_list => [
		      "ACRDBT Index"
		    ],
		  },
		  'Date' => { 
		    :comparison_operator => 'BETWEEN', 
		    :attribute_value_list => [
		      '2012-01-01', '2012-12-31'
		    ]
		  } 
		}
	})

	@debug = dynamodb.describe_table ({:table_name => '2012'})
	# @data = [{:time => 0, :value => 10}]
	if params['format'] == "html"
		erb :index 
	elsif params['format'] == "json"
		content_type :json
		@data.items.to_json
	end
		
end