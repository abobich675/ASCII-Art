-- CreateTable
CREATE TABLE "Post" (
    "id" SERIAL NOT NULL,
    "title" TEXT,
    "prompt" TEXT,
    "user" TEXT,
    "path" TEXT NOT NULL,
    "gallery" BOOLEAN NOT NULL DEFAULT false,
    "style" TEXT NOT NULL,

    CONSTRAINT "Post_pkey" PRIMARY KEY ("id")
);
