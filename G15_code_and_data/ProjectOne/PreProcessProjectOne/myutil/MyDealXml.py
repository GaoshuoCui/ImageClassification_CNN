from xml.dom import minidom


class MyDealXml:

    @staticmethod
    def readXml(path):
        dom = minidom.parse(path)
        root = dom.documentElement
        names = root.getElementsByTagName('Name')
        for name in names:
            # 它的第一个子节点是一个textnode，存取的是真正的节点值
            print(name.childNodes[0].nodeValue, end='\t')
            if name.hasAttribute('age'):
                print(name.getAttribute('age'), end='\t')
            print('')
            return None