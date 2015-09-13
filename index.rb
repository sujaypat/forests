require 'sinatra'
require 'aws-sdk-core'
require 'json'

get	"/" do 
	erb :index
end

# get "/:ticker?.:format?" do
# 	dynamodb = Aws::DynamoDB::Client.new(
# 		region: 'us-east-1',
# 		credentials: Aws::Credentials.new('AKIAI6PU7IIGNUBSI26A', 'qBrlCJMywo029GlaXsLVI8Rf4286eWsC6aU+ue53')
# 	)

# 	@data = dynamodb.query({
# 		:table_name => "Catalog", 
# 		:consistent_read => true,
# 		:select => 'ALL_ATTRIBUTES',
# 		:key_conditions => { 
# 		  'Ticker' => { 
# 		    :comparison_operator => 'EQ', 
# 		    :attribute_value_list => [
# 		      params["ticker"]
# 		    ]
# 		  }
# 		}
# 	})
# 	if params['format'] == "json"
# 		content_type :json
# 		@data.items.to_json
# 	end
# end

get "/:year/:ticker?.:format?" do
	# dynamodb = Aws::DynamoDB::Client.new(
	# 	region: 'us-east-1',
	# 	credentials: Aws::Credentials.new('AKIAI6PU7IIGNUBSI26A', 'qBrlCJMywo029GlaXsLVI8Rf4286eWsC6aU+ue53')
	# )

	# @data = dynamodb.query({
	# 	:table_name => params["year"], 
	# 	:consistent_read => true,
	# 	:select => 'ALL_ATTRIBUTES',
	# 	:key_conditions => { 
	# 	  'Ticker' => { 
	# 	    :comparison_operator => 'EQ', 
	# 	    :attribute_value_list => [
	# 	      params["ticker"] + " Index"
	# 	    ],
	# 	  },
	# 	  'Date' => { 
	# 	    :comparison_operator => 'BETWEEN', 
	# 	    :attribute_value_list => [
	# 	      params["year"]+'-01-01', params["year"]+'-12-31'
	# 	    ]
	# 	  } 
	# 	}
	# })

	
	# if params['format'] == "json"
	# 	content_type :json
	# 	@data.items.to_json
	# else
		erb :view
	# end
		
end

get "/migrateToParse" do
	File.read('transferToParse.html')
end