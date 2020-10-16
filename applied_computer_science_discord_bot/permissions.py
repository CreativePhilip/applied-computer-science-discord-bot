from discord import Message, Member


def has_role(role):
    """
    Method for performing permission checking
    :param role: string or a list of strings representing a role name
    """
    def _has_role(func):
        def wrapper(self, *args, **kwargs):
            msg: Message = kwargs['message']
            author: Member = msg.author

            kwargs.update({"is_auth": _rank_in_list(role, author.roles)}
                          if type(role) is str else _ranks_in_list(role, author.roles))
            return func(self, *args, **kwargs)

        return wrapper

    return _has_role


def _rank_in_list(name, roles) -> bool:
    """
    Checks if a given name is roles
    :param name: string of a role name
    :param roles: list of roles, obtained from the member class
    :return: True if name is contained in roles list else False
    """
    for role in roles:
        if name == role.name:
            return True
    return False


def _ranks_in_list(name_list, roles) -> bool:
    """
    Checks if any name is present in the roles list
    :param name_list: list of string representing a discord role
    :param roles: list of roles, obtained from the member class
    :return: True if any name is contained in roles list else False
    """
    for role in roles:
        if role.name in name_list:
            return True
    return False
