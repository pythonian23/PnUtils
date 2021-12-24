import threading
import ez_api as ez


def get_mil(n_id, key):
    builds = get_builds(n_id, key)
    mils = set()
    for build in builds:
        mil = (
            build["imp_barracks"],
            build["imp_factory"],
            build["imp_hangar"],
            build["imp_drydock"]
        )
        mils.add(mil)
    return mils


def get_builds(n_id, key):
    cities = get_cities(n_id, key)
    builds = []
    threads = []
    for city in cities:
        threads.append(threading.Thread(
            target=(lambda x, y: builds.append(ez.req(x, y))),
            args=(f"city/id={city}", key)
        ))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return builds


def get_cities(n_id, key):
    return ez.req(f"nation/id={n_id}/", key)["cityids"]


if __name__ == "__main__":
    n_id = input("Nation ID: ")
    key = input("API Key: ")
    print(get_mil(n_id, key))
