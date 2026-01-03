#!/usr/bin/env ruby
require 'yaml'
require 'fileutils'

# Load the YAML file
yaml_file = File.join(__dir__, 'hvac.yaml')
data = YAML.load_file(yaml_file)

# Output directory
content_dir = File.join(__dir__, 'hugo', 'content')
FileUtils.mkdir_p(content_dir)

# Helper to convert snake_case to Title Case
def titleize(text)
  text.to_s.split('_').map(&:capitalize).join(' ')
end

# Helper to create URL-friendly slugs
def slugify(text)
  text.to_s.downcase.gsub(/[^a-z0-9]+/, '-').gsub(/-+$/, '').gsub(/^-+/, '')
end

# Generate weight based on index for ordering
def generate_frontmatter(title, weight, section = nil)
  frontmatter = "---\n"
  frontmatter += "title: \"#{title}\"\n"
  frontmatter += "weight: #{weight}\n"
  frontmatter += "section: \"#{section}\"\n" if section
  frontmatter += "---\n\n"
  frontmatter
end

# Process nested structure
def process_node(data, path = [], parent_dir = '', weight = 0)
  case data
  when Hash
    data.each_with_index do |(key, value), index|
      current_path = path + [key]
      slug = slugify(key)
      title = titleize(key)

      # Create directory for this section
      section_dir = File.join(parent_dir, slug)
      FileUtils.mkdir_p(section_dir)

      # Create _index.md for this section
      index_file = File.join(section_dir, '_index.md')
      content = generate_frontmatter(title, index + 1)

      # Add description if available
      if value.is_a?(Hash) && value['description']
        content += "#{value['description']}\n\n"
      end

      # Add version if available
      if value.is_a?(Hash) && value['version']
        content += "*Version: #{value['version']}*\n\n"
      end

      File.write(index_file, content)
      puts "Created: #{index_file}"

      # Process children
      if value.is_a?(Hash)
        # Filter out metadata keys
        child_data = value.reject { |k, v| ['description', 'version'].include?(k) }
        process_node(child_data, current_path, section_dir, 0) unless child_data.empty?
      elsif value.is_a?(Array)
        # Create a content file listing the items
        items_content = generate_frontmatter(title, index + 1)
        items_content += "## Components\n\n"
        value.each do |item|
          items_content += "- #{titleize(item)}\n"
        end
        File.write(index_file, items_content)
      end
    end
  when Array
    # If we get an array at the top level, process each item
    data.each_with_index do |item, index|
      if item.is_a?(String)
        # Skip - arrays of strings are handled by parent
      else
        process_node(item, path, parent_dir, index)
      end
    end
  end
end

# Start processing from the root
if data['hvac']
  # Create root index
  root_index = File.join(content_dir, '_index.md')
  root_content = generate_frontmatter('HVAC Systems Encyclopedia', 1)
  root_content += "# HVAC Systems Encyclopedia\n\n"
  root_content += "A comprehensive guide to heating, ventilation, and air conditioning systems.\n\n"
  File.write(root_index, root_content)
  puts "Created: #{root_index}"

  # Process all main sections
  process_node(data['hvac'], ['hvac'], content_dir, 0)
else
  puts "Error: 'hvac' key not found in YAML file"
  exit 1
end

puts "\nContent generation complete!"
puts "Total files created in #{content_dir}"
