import threading
import tools.nation as nation
import tools.ez_api as ez


def get_mil(aa_id, key):
    batch = 16
    nations = get_nations(aa_id, key)
    mils = {}
    threads = []
    for i in range(len(nations)):
        threads.append(threading.Thread(
            target=(lambda x, y, z: mils.update({nations[z]: nation.get_mil(x, y)})),
            args=(nations[i], key, i)
        ))
        threads[-1].start()
        if i%batch == batch-1 or i == len(nations)-1:
            for ignore in threads:
                threads.pop(0).join()

    return mils


def get_nations(aa_id, key):
    return ez.req(f"alliance/id={aa_id}", key)["member_id_list"]


if __name__ == "__main__":
    aa_id = input("Alliance ID: ")
    key = input("API Key: ")
    print(get_mil(aa_id, key))
