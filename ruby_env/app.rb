require 'sinatra'
require 'sinatra/activerecord'
require 'sinatra/json'
require 'sinatra/reloader' if development?

# Set up database connection
set :database_file, 'config/database.yml'

# Define Item model
class Item < ActiveRecord::Base
  validates :name, presence: true
end

# Configure application
configure do
  set :public_folder, 'public'
  set :views, 'views'
  enable :sessions
end

# Enable CORS
before do
  content_type :json
  headers 'Access-Control-Allow-Origin' => '*',
          'Access-Control-Allow-Methods' => ['OPTIONS', 'GET', 'POST', 'PUT', 'DELETE'],
          'Access-Control-Allow-Headers' => 'Content-Type'
end

options '*' do
  response.headers['Allow'] = 'HEAD,GET,PUT,POST,DELETE,OPTIONS'
  response.headers['Access-Control-Allow-Headers'] = 'X-Requested-With, X-HTTP-Method-Override, Content-Type, Cache-Control, Accept'
  200
end

# Root route
get '/' do
  json message: 'Welcome to the Interview API'
end

# Get all items
get '/items' do
  items = Item.all
  json items
end

# Get item by id
get '/items/:id' do
  item = Item.find_by_id(params[:id])
  if item
    json item
  else
    status 404
    json error: 'Item not found'
  end
end

# Create new item
post '/items' do
  data = JSON.parse(request.body.read)
  item = Item.new(name: data['name'], description: data['description'])
  
  if item.save
    status 201
    json item
  else
    status 422
    json error: item.errors.full_messages
  end
end

# Update item
put '/items/:id' do
  item = Item.find_by_id(params[:id])
  
  if item
    data = JSON.parse(request.body.read)
    if item.update(name: data['name'], description: data['description'])
      json item
    else
      status 422
      json error: item.errors.full_messages
    end
  else
    status 404
    json error: 'Item not found'
  end
end

# Delete item
delete '/items/:id' do
  item = Item.find_by_id(params[:id])
  
  if item
    item.destroy
    status 204
  else
    status 404
    json error: 'Item not found'
  end
end
