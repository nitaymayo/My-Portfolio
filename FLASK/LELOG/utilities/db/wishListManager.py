from utilities.db.db_manager import dbManager


class WishListManager:
    def exist(self, user_id, product_id):
        if len(dbManager.fetch("select * from wish_lists as w where w.customer_ID=%s and w.product_ID=%s" % (user_id, product_id))) > 0:
            return True
        else:
            return False

    def insert(self, user_id, product_id):
        dbManager.commit("insert into wish_lists values (%s,%s)" % (user_id, product_id))

    def delete(self, user_id, product_id):
        if wishListManager.exist(user_id, product_id):
            dbManager.commit("delete from wish_lists as w where w.customer_ID=%s and w.product_ID=%s" % (user_id, product_id))
        else:
            return False

    def deleteAllFor(self, user_id):
        dbManager.commit("delete from wish_lists as w where w.customer_ID=%s" % (user_id,))

    def getFavorites(self, user_id):
        return dbManager.fetch("select p.Product_ID, p.Name, p.Price from wish_lists as w join products as p on w.Product_ID=p.Product_ID where w.customer_id=%s" % (user_id))


# Creates an instance for the DBManager class for export.
wishListManager = WishListManager()