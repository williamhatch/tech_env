class CreateItems < ActiveRecord::Migration[7.1]
  def change
    create_table :items do |t|
      t.string :name, null: false
      t.text :description
      t.boolean :active, default: true
      
      t.timestamps
    end
    
    add_index :items, :name
  end
end
