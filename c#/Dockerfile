FROM bitnami/dotnet-sdk

COPY . .

RUN dotnet build
ENV ASPNETCORE_URLS="http://0.0.0.0:5000"

ENTRYPOINT [ "dotnet", "./bin/Debug/net7.0/c#.dll" ]