FROM mcr.microsoft.com/mssql/server:2019-latest

# Create a config directory
RUN mkdir -p /usr/config
WORKDIR /usr/config

# Bundle config source
COPY . /usr/config

# Grant permissions for to our scripts to be executable
# RUN chmod +x /usr/config/entrypoint.sh
# RUN chmod +x /usr/config/configure-db.sh
RUN chmod +x /usr/config/setup.sh


ENTRYPOINT ["./setup.sh"]