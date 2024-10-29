# Use a lightweight web server image
FROM nginx:alpine

# Copy website files to the NGINX HTML directory
COPY app/ /usr/share/nginx/html

# Expose port 80 for web traffic
EXPOSE 80
