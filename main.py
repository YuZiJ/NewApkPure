from core.api import Api

api = Api()

# y = api.search('vpn', first=False, all_page=False)
# print(y.to_dict())

print("开始访问 ApkPure")
y = api.search("com.tencent.mm", first=True, all_page=False)
dict = y.to_dict()
app_name = dict['app_name'][0]
version = dict['version'][0]
package_name = dict['package_name'][0]
print(f'app_name: {app_name}, version: {version}, package_name: {package_name}')

# api.download(y, count=1)