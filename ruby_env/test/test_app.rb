require_relative 'test_helper'
require 'rack/test'
require_relative '../app'

class TestApp < Minitest::Test
  include Rack::Test::Methods

  def app
    Sinatra::Application
  end

  def setup
    # Clear the database before each test
    Item.destroy_all
  end

  def test_root_endpoint
    get '/'
    assert_equal 200, last_response.status
    response = JSON.parse(last_response.body)
    assert_equal 'Welcome to the Interview API', response['message']
  end

  def test_create_item
    post '/items', { name: 'Test Item', description: 'This is a test item' }.to_json
    assert_equal 201, last_response.status
    response = JSON.parse(last_response.body)
    assert_equal 'Test Item', response['name']
    assert_equal 'This is a test item', response['description']
    assert response['id']
  end

  def test_get_all_items
    # Create some test items
    item1 = Item.create(name: 'Item 1', description: 'First item')
    item2 = Item.create(name: 'Item 2', description: 'Second item')

    get '/items'
    assert_equal 200, last_response.status
    response = JSON.parse(last_response.body)
    assert_equal 2, response.length
    assert_equal 'Item 1', response[0]['name']
    assert_equal 'Item 2', response[1]['name']
  end

  def test_get_item_by_id
    # Create a test item
    item = Item.create(name: 'Test Item', description: 'This is a test item')

    get "/items/#{item.id}"
    assert_equal 200, last_response.status
    response = JSON.parse(last_response.body)
    assert_equal 'Test Item', response['name']
    assert_equal 'This is a test item', response['description']
  end

  def test_get_nonexistent_item
    get '/items/999'
    assert_equal 404, last_response.status
    response = JSON.parse(last_response.body)
    assert_equal 'Item not found', response['error']
  end

  def test_update_item
    # Create a test item
    item = Item.create(name: 'Original Name', description: 'Original description')

    put "/items/#{item.id}", { name: 'Updated Name', description: 'Updated description' }.to_json
    assert_equal 200, last_response.status
    response = JSON.parse(last_response.body)
    assert_equal 'Updated Name', response['name']
    assert_equal 'Updated description', response['description']
  end

  def test_update_nonexistent_item
    put '/items/999', { name: 'Updated Name' }.to_json
    assert_equal 404, last_response.status
    response = JSON.parse(last_response.body)
    assert_equal 'Item not found', response['error']
  end

  def test_delete_item
    # Create a test item
    item = Item.create(name: 'Item to Delete')

    delete "/items/#{item.id}"
    assert_equal 204, last_response.status
    assert_nil Item.find_by_id(item.id)
  end

  def test_delete_nonexistent_item
    delete '/items/999'
    assert_equal 404, last_response.status
    response = JSON.parse(last_response.body)
    assert_equal 'Item not found', response['error']
  end
end
