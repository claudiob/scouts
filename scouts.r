# Plot watchers per repository as PNG graph

watchers_per_repo <- read.csv("watchers_per_repo.csv")

png(file="watchers_per_repo.png", bg="white",width=600,height=450)
plot(watchers_per_repo, xlab="Watchers", ylab="Repositories", main="Watchers per repository", bg=rgb(0.75,0.75,1), col=rgb(0,0,0.5), cex.main=1.5, cex.lab=1.3, pch=21, type="o",family="AvenirLTStd-Book")
dev.off()

# Also plot a detail limited to 1~30 watchers
png(file="watchers_per_repo_detail.png", bg="white",width=600,height=450)
plot(watchers_per_repo[1:30,], xlab="Watchers", ylab="Repositories", main="Watchers per repository (limited to 1~30)", bg=rgb(0.75,0.75,1), col=rgb(0,0,0.5), cex.main=1.5, cex.lab=1.3, pch=21, type="o",family="AvenirLTStd-Book")
dev.off()

# Plot watchers per creation date as PNG graph

users_per_date <- read.csv("users_per_date.csv")

png(file="users_per_date.png", bg="white",width=600,height=450)
plot(users_per_date[,2], xlab="Creation date", ylab="Users", main="Users per creation date", bg=rgb(0.75,0.75,1), col=rgb(0,0,0.5), cex.main=1.5, cex.lab=1.3, pch=21, type="o",family="AvenirLTStd-Book",xaxt="n")
axis(1,  4, users_per_date[,1][4])
axis(1, 10, users_per_date[,1][10])
axis(1, 16, users_per_date[,1][16])
axis(1, 22, users_per_date[,1][22])
axis(1, 28, users_per_date[,1][28])
axis(1, 34, users_per_date[,1][34])
dev.off()