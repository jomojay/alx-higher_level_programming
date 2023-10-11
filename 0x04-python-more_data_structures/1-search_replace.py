#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def sr_elm(elm):
        return (replace if elm == search else elm)
    return list(map(sr_elm, my_list))
