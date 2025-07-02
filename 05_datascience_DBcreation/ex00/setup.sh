# Database creation
sudo -u postgres psql -c 'create database piscineds'

# Create user with encrypted password
sudo -u postgres psql -c 'create user sleleu with encrypted password "mysecretpassword"'